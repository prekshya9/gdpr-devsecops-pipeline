const express = require('express');
const app = express();
app.use(express.json());

const users = [];

// VULNERABILITY 1 (GDPR Art. 25/32): Logging unencrypted PII (Email & Credit Card) in plain text
app.post('/api/v1/register', (req, res) => {
    const { username, email, creditCard } = req.body;
    
    // Violation: Direct logging of sensitive user data to logs
    console.log(`[USER REGISTRATION LOG] Processing account for Email: ${email} | Card: ${creditCard}`);
    
    users.push({ username, email, creditCard });
    return res.status(201).json({ message: "User registered successfully", userId: users.length - 1 });
});

// VULNERABILITY 2: Returning unencrypted sensitive PII via endpoint
app.get('/api/v1/user/:id', (req, res) => {
    const user = users[req.params.id];
    if (!user) return res.status(404).json({ error: "User not found" });
    return res.json(user);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));