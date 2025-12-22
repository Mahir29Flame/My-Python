// Daily Journal App - JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const journalText = document.getElementById('journal-text');
    const dateInput = document.getElementById('date-input');
    const saveBtn = document.getElementById('save-btn');
    const clearBtn = document.getElementById('clear-btn');
    const newEntryBtn = document.getElementById('new-entry');
    const themeToggle = document.getElementById('theme-toggle');
    const settingsBtn = document.getElementById('settings-btn');
    const modal = document.getElementById('settings-modal');
    const closeModal = document.querySelector('.close');
    const themeSelect = document.getElementById('theme-select');
    const fontSelect = document.getElementById('font-select');
    const fontSizeSlider = document.getElementById('font-size');
    const fontSizeValue = document.getElementById('font-size-value');
    const bgPatternSelect = document.getElementById('bg-pattern');
    const accentColorInput = document.getElementById('accent-color');
    const exportLogsBtn = document.getElementById('export-logs');
    const entriesList = document.getElementById('entries-list');
    const saveSettingsBtn = document.querySelector('.save-settings');
    
    // Initialize date to today in dd/mm/yy format
    const today = new Date();
    const day = String(today.getDate()).padStart(2, '0');
    const month = String(today.getMonth() + 1).padStart(2, '0'); // January is 0!
    const year = String(today.getFullYear()).slice(-2);
    const displayDate = `${day}/${month}/${year}`;
    dateInput.value = displayDate;
    
    // Load saved data
    loadSettings();
    // Load the entry for today's date when the app starts
    setTimeout(() => {
        // Set today's date in dd/mm/yy format
        const today = new Date();
        const day = String(today.getDate()).padStart(2, '0');
        const month = String(today.getMonth() + 1).padStart(2, '0');
        const year = String(today.getFullYear()).slice(-2);
        dateInput.value = `${day}/${month}/${year}`;
        
        loadEntryForDate();
        updateEntriesList(); // Populate the entries list
        
        // Ensure editor has focus after loading
        journalText.focus();
    }, 100); // Small delay to ensure DOM is ready
    
    // Event Listeners
    dateInput.addEventListener('change', function() {
        // Validate date format dd/mm/yy
        const dateRegex = /^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/\d{2}$/;
        if (dateRegex.test(dateInput.value)) {
            loadEntryForDate();
        } else {
            // If invalid format, revert to current date
            const today = new Date();
            const day = String(today.getDate()).padStart(2, '0');
            const month = String(today.getMonth() + 1).padStart(2, '0');
            const year = String(today.getFullYear()).slice(-2);
            dateInput.value = `${day}/${month}/${year}`;
            loadEntryForDate();
        }
    });
    saveBtn.addEventListener('click', saveEntry);
    clearBtn.addEventListener('click', clearEntry);
    newEntryBtn.addEventListener('click', createNewEntry);
    themeToggle.addEventListener('click', toggleTheme);
    settingsBtn.addEventListener('click', openSettings);
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            closeSettings();
        }
    });
    
    // Resizable sidebar functionality
    const sidebar = document.querySelector('.md3-navigation-drawer');
    const resizeHandle = document.querySelector('.resize-handle');
    let isResizing = false;

    if (resizeHandle) {
        resizeHandle.addEventListener('mousedown', function(e) {
            isResizing = true;
            document.body.style.userSelect = 'none';
            e.preventDefault();
        });

        document.addEventListener('mousemove', function(e) {
            if (!isResizing) return;
            const container = document.querySelector('.md3-container');
            const containerRect = container.getBoundingClientRect();
            const newWidth = e.clientX - containerRect.left;
            
            // Set min and max width constraints
            if (newWidth > 200 && newWidth < 600) {
                sidebar.style.width = newWidth + 'px';
            }
        });

        document.addEventListener('mouseup', function() {
            isResizing = false;
            document.body.style.userSelect = '';
        });
    }
    
    themeSelect.addEventListener('change', updateTheme);
    fontSelect.addEventListener('change', updateFontFamily);
    fontSizeSlider.addEventListener('input', updateFontSize);
    bgPatternSelect.addEventListener('change', updateBgPattern);
    accentColorInput.addEventListener('input', updateAccentColor);
    exportLogsBtn.addEventListener('click', () => window.exportLogs());
    if (saveSettingsBtn) {
        saveSettingsBtn.addEventListener('click', closeSettings);
    }
    
    // Set up all close dialog button listeners after the DOM elements are available
    setTimeout(() => {
        const closeDialogButtons = document.querySelectorAll('.close-dialog');
        closeDialogButtons.forEach(button => {
            button.addEventListener('click', closeSettings);
        });
    }, 0);
    
    // Update content when user types in the editor (for auto-save)
    journalText.addEventListener('input', function() {
        // Optionally implement auto-save if desired
    });
    
    // Functions
    function toggleTheme() {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'cyan-black';
        const themes = ['cyan-black', 'dark', 'blue', 'green'];
        const currentIndex = themes.indexOf(currentTheme);
        const nextIndex = (currentIndex + 1) % themes.length;
        const nextTheme = themes[nextIndex];
        
        document.documentElement.setAttribute('data-theme', nextTheme);
        localStorage.setItem('theme', nextTheme);
        logAction(`Theme changed to ${nextTheme}`);
        
        // Update the theme selector in settings
        themeSelect.value = nextTheme;
    }
    
    function formatDateForStorage(dateString) {
        // Convert dd/mm/yy to YYYY-MM-DD for storage
        if (!dateString || dateString.indexOf('/') === -1) {
            // If it's already in YYYY-MM-DD format, return as is
            return dateString;
        }
        
        const parts = dateString.split('/');
        if (parts.length !== 3) {
            // Return current date if format is invalid
            const today = new Date();
            const year = today.getFullYear();
            const month = String(today.getMonth() + 1).padStart(2, '0');
            const day = String(today.getDate()).padStart(2, '0');
            return `${year}-${month}-${day}`;
        }
        
        const [day, month, year] = parts;
        // Convert 2-digit year to 4-digit (assuming current century if less than 50)
        const fullYear = parseInt(year) < 50 ? `20${year}` : `19${year}`;
        return `${fullYear}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`;
    }

    function formatDateForDisplay(dateString) {
        // Convert YYYY-MM-DD to dd/mm/yy for display
        if (!dateString || dateString.indexOf('-') === -1) {
            // If it's already in dd/mm/yy format, return as is
            return dateString;
        }
        
        const [year, month, day] = dateString.split('-');
        const shortYear = year.slice(-2);
        return `${day}/${month}/${shortYear}`;
    }

    function loadEntryForDate() {
        const date = formatDateForStorage(dateInput.value); // Convert dd/mm/yy to YYYY-MM-DD for storage
        const entry = localStorage.getItem(`journal_${date}`);
        
        if (entry) {
            journalText.value = entry;
        } else {
            journalText.value = '';
        }
    }
    
    function saveEntry() {
        const date = formatDateForStorage(dateInput.value); // Convert dd/mm/yy to YYYY-MM-DD for storage
        const content = journalText.value; // Get text content from textarea
        
        if (date && content.trim() !== '') { // Check if not empty
            localStorage.setItem(`journal_${date}`, content);
            logAction(`Journal entry saved for ${dateInput.value}`);
            showNotification('Entry saved successfully!');
        } else if (date && content.trim() === '') {
            // If content is empty, remove the entry
            localStorage.removeItem(`journal_${date}`);
            logAction(`Journal entry deleted for ${dateInput.value}`);
            showNotification('Entry removed!');
        }
        
        // Refresh entries list
        updateEntriesList();
    }
    
    function clearEntry() {
        if (confirm("Are you sure you want to remove this journal entry?")) {
            const date = formatDateForStorage(dateInput.value);
            // Remove the entry from storage
            localStorage.removeItem(`journal_${date}`);
            logAction(`Journal entry removed for ${dateInput.value}`);
            showNotification('Entry removed!');
            
            // Clear the text area
            journalText.value = '';
            
            // Refresh the entries list
            updateEntriesList();
        }
    }
    
    function createNewEntry() {
        // Set to today's date in dd/mm/yy format
        const today = new Date();
        const day = String(today.getDate()).padStart(2, '0');
        const month = String(today.getMonth() + 1).padStart(2, '0');
        const year = String(today.getFullYear()).slice(-2);
        dateInput.value = `${day}/${month}/${year}`;
        
        // Clear the text area for a new entry
        journalText.value = '';
        journalText.focus();
    }
    
    function createNewEntry() {
        journalText.value = '';
        journalText.focus();
    }
    
    function toggleTheme() {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'cyan-black';
        const themes = ['cyan-black', 'dark', 'blue', 'green'];
        const currentIndex = themes.indexOf(currentTheme);
        const nextIndex = (currentIndex + 1) % themes.length;
        const nextTheme = themes[nextIndex];
        
        document.documentElement.setAttribute('data-theme', nextTheme);
        localStorage.setItem('theme', nextTheme);
        logAction(`Theme changed to ${nextTheme}`);
    }
    
    function updateTheme() {
        const selectedTheme = themeSelect.value;
        document.documentElement.setAttribute('data-theme', selectedTheme);
        localStorage.setItem('theme', selectedTheme);
        logAction(`Theme changed to ${selectedTheme} via settings`);
    }
    
    function updateFontFamily() {
        const selectedFont = fontSelect.value;
        document.documentElement.style.setProperty('--font-family', getFontFamily(selectedFont));
        localStorage.setItem('font-family', selectedFont);
        logAction(`Font changed to ${selectedFont}`);
    }
    
    function updateFontSize() {
        const fontSize = fontSizeSlider.value + 'px';
        document.documentElement.style.setProperty('--font-size', fontSize);
        fontSizeValue.textContent = fontSize;
        localStorage.setItem('font-size', fontSizeSlider.value);
        logAction(`Font size changed to ${fontSize}`);
    }
    
    function getFontFamily(fontType) {
        switch(fontType) {
            case 'serif': return "'Times New Roman', Times, serif";
            case 'sans-serif': return "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif";
            case 'monospace': return "'Courier New', Courier, monospace";
            default: return "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif";
        }
    }
    
    function updateBgPattern() {
        const selectedPattern = bgPatternSelect.value;
        const journalElement = document.getElementById('journal-text');
        
        // Remove all pattern classes
        journalElement.classList.remove('bg-pattern-lined', 'bg-pattern-grid', 'bg-pattern-dots');
        
        if (selectedPattern !== 'none') {
            journalElement.classList.add(`bg-pattern-${selectedPattern}`);
        }
        
        localStorage.setItem('bg-pattern', selectedPattern);
        logAction(`Background pattern changed to ${selectedPattern}`);
    }
    
    function updateAccentColor() {
        const color = accentColorInput.value;
        document.documentElement.style.setProperty('--btn-primary-bg', color);
        localStorage.setItem('accent-color', color);
        logAction(`Accent color changed to ${color}`);
    }
    

    
    function updateEntriesList() {
        // Get all journal entries from localStorage
        const entries = [];
        for (let i = 0; i < localStorage.length; i++) {
            const key = localStorage.key(i);
            // Filter out log entries - only include journal entries (not logs)
            if (key && key.startsWith('journal_') && !key.includes('logs')) {
                const date = key.replace('journal_', '');
                const content = localStorage.getItem(key);
                // Get a preview of the content (first 60 characters)
                const preview = content.length > 60 ? content.substring(0, 60) + '...' : content;
                
                entries.push({
                    date: date,
                    content: content,
                    preview: preview
                });
            }
        }
        
        // Sort entries by date (newest first)
        entries.sort((a, b) => {
            // Convert date strings to Date objects for proper comparison
            return new Date(b.date) - new Date(a.date);
        });
        
        // Clear the entries list
        entriesList.innerHTML = '';
        
        // Add each entry to the list
        entries.forEach(entry => {
            const entryElement = document.createElement('div');
            entryElement.className = 'entry-item';
            if (formatDateForStorage(dateInput.value) === entry.date) {
                entryElement.classList.add('active');
            }
            
            // Format the date for display as dd/mm/yy
            const displayDate = formatDateForDisplay(entry.date);
            
            entryElement.innerHTML = `
                <div class="entry-date">${displayDate}</div>
                <div class="entry-preview">${entry.preview || '<em>Empty entry</em>'}</div>
            `;
            
            entryElement.addEventListener('click', () => {
                // Remove active class from all entries
                document.querySelectorAll('.entry-item').forEach(item => {
                    item.classList.remove('active');
                });
                
                // Add active class to clicked entry
                entryElement.classList.add('active');
                
                // Load the entry content
                dateInput.value = formatDateForDisplay(entry.date);
                journalText.value = entry.content;
            });
            
            entriesList.appendChild(entryElement);
        });
        
        // Show message if no entries
        if (entries.length === 0) {
            entriesList.innerHTML = '<div class="no-entries">No entries yet. Start writing!</div>';
        }
    }
    
    function setupCloseDialogButtons() {
        const closeDialogButtons = document.querySelectorAll('.close-dialog');
        closeDialogButtons.forEach(button => {
            // Remove any existing listeners to avoid duplicates
            const newButton = button.cloneNode(true);
            button.parentNode.replaceChild(newButton, button);
            newButton.addEventListener('click', closeSettings);
        });
    }
    
    function openSettings() {
        modal.style.display = 'block';
        setupCloseDialogButtons(); // Set up listeners when modal opens
    }
    
    function closeSettings() {
        modal.style.display = 'none';
    }
    
    function loadSettings() {
        // Load theme
        const savedTheme = localStorage.getItem('theme') || 'cyan-black';
        document.documentElement.setAttribute('data-theme', savedTheme);
        themeSelect.value = savedTheme;
        
        // Load font family
        const savedFont = localStorage.getItem('font-family') || 'default';
        fontSelect.value = savedFont;
        document.documentElement.style.setProperty('--font-family', getFontFamily(savedFont));
        
        // Load font size
        const savedFontSize = localStorage.getItem('font-size') || '16';
        fontSizeSlider.value = savedFontSize;
        fontSizeValue.textContent = savedFontSize + 'px';
        document.documentElement.style.setProperty('--font-size', savedFontSize + 'px');
        
        // Load background pattern
        const savedPattern = localStorage.getItem('bg-pattern') || 'none';
        bgPatternSelect.value = savedPattern;
        if (savedPattern !== 'none') {
            document.getElementById('journal-text').classList.add(`bg-pattern-${savedPattern}`);
        }
        
        // Load accent color
        const savedColor = localStorage.getItem('accent-color') || '#0d6efd';
        accentColorInput.value = savedColor;
        document.documentElement.style.setProperty('--btn-primary-bg', savedColor);
    }
    
    function logAction(action) {
        // Create log entry
        const timestamp = new Date().toISOString();
        const logEntry = `[${timestamp}] ${action}\n`;
        
        // Append to a log file-like structure in localStorage
        const existingLogs = localStorage.getItem('journal_logs') || '';
        localStorage.setItem('journal_logs', existingLogs + logEntry);
        
        // For actual file logging, we'll handle that differently (see next function)
        logToFile(action);
    }
    
    function logToFile(action) {
        // Send log to server to write to file
        fetch('/api/log', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: action })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Log sent to server:', data);
        })
        .catch(error => {
            console.error('Error sending log to server:', error);
            // Fallback to localStorage if server is not available
            const timestamp = new Date().toISOString();
            const logEntry = `[${timestamp}] ${action}\n`;
            
            const existingLogs = localStorage.getItem('journal_logs_file') || '';
            localStorage.setItem('journal_logs_file', existingLogs + logEntry);
        });
    }
    
    function showNotification(message) {
        // Create a simple notification element
        const notification = document.createElement('div');
        notification.textContent = message;
        notification.style.position = 'fixed';
        notification.style.bottom = '20px';
        notification.style.right = '20px';
        notification.style.backgroundColor = '#0d6efd';
        notification.style.color = 'white';
        notification.style.padding = '10px 20px';
        notification.style.borderRadius = '4px';
        notification.style.zIndex = '1000';
        notification.style.boxShadow = '0 4px 6px rgba(0,0,0,0.1)';
        
        document.body.appendChild(notification);
        
        // Remove after 3 seconds
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 3000);
    }
    
    // Add a method to export logs as a file
    window.exportLogs = function() {
        // Try to download from server first
        fetch('/api/export-logs')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.blob();
        })
        .then(blob => {
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'journal_logs.txt';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        })
        .catch(error => {
            console.error('Error exporting logs from server:', error);
            // Fallback: try to export from localStorage
            const logs = localStorage.getItem('journal_logs_file') || '';
            if (logs) {
                const blob = new Blob([logs], { type: 'text/plain' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'journal_logs_local.txt';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
            } else {
                alert('No logs to export');
            }
        });
    };
});