const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();
const PORT = 3000;

// Middleware
app.use(express.json());
app.use(express.static('.')); // Serve static files from root

// Create logs directory if it doesn't exist
const logsDir = path.join(__dirname, 'logs');
if (!fs.existsSync(logsDir)) {
    fs.mkdirSync(logsDir, { recursive: true });
}

// API endpoint to write log entries to file
app.post('/api/log', (req, res) => {
    const { message } = req.body;
    const timestamp = new Date().toISOString();
    const logEntry = `[${timestamp}] ${message}\n`;
    
    const logFilePath = path.join(logsDir, 'journal.log');
    
    fs.appendFile(logFilePath, logEntry, (err) => {
        if (err) {
            console.error('Error writing to log file:', err);
            res.status(500).json({ error: 'Failed to write log' });
        } else {
            console.log('Log entry added:', logEntry.trim());
            res.status(200).json({ success: true });
        }
    });
});

// API endpoint to get recent logs
app.get('/api/logs', (req, res) => {
    const logFilePath = path.join(logsDir, 'journal.log');
    
    fs.readFile(logFilePath, 'utf8', (err, data) => {
        if (err) {
            if (err.code === 'ENOENT') {
                // File doesn't exist yet, return empty array
                res.json([]);
            } else {
                console.error('Error reading log file:', err);
                res.status(500).json({ error: 'Failed to read logs' });
            }
        } else {
            // Split the log data into individual entries
            const logEntries = data.trim().split('\n').filter(line => line).reverse().slice(0, 50); // Last 50 entries
            res.json(logEntries);
        }
    });
});

// API endpoint to export logs
app.get('/api/export-logs', (req, res) => {
    const logFilePath = path.join(logsDir, 'journal.log');
    
    if (fs.existsSync(logFilePath)) {
        res.download(logFilePath, 'journal_logs.txt', (err) => {
            if (err) {
                console.error('Error exporting logs:', err);
                res.status(500).json({ error: 'Failed to export logs' });
            }
        });
    } else {
        res.status(404).json({ error: 'Log file not found' });
    }
});

app.listen(PORT, () => {
    console.log(`Journal app server running on http://localhost:${PORT}`);
    console.log(`Logs will be saved to: ${logsDir}`);
});