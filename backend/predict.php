<?php
require_once 'config.php';

// Set response header to JSON
header('Content-Type: application/json');

// Only allow POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode(['success' => false, 'error' => 'Only POST requests allowed']);
    exit;
}

// Get text from frontend
$input = json_decode(file_get_contents('php://input'), true);
$text = isset($input['text']) ? trim($input['text']) : '';

// Validate input
if (empty($text)) {
    echo json_encode(['success' => false, 'error' => 'Please enter some text.']);
    exit;
}

// Call Python Flask API using cURL
$ch = curl_init(PYTHON_API_URL . '/predict');
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode(['text' => $text]));
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT, API_TIMEOUT);

$response = curl_exec($ch);
$error    = curl_error($ch);
curl_close($ch);

// Handle cURL errors (Python server not running)
if ($error) {
    echo json_encode([
        'success' => false,
        'error'   => 'Could not connect to ML model. Make sure Python server is running.'
    ]);
    exit;
}

// Return Python API response directly to frontend
echo $response;
?>
