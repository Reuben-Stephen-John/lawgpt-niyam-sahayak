const lawgpt = async (prompt) => {
    try {
      const url = 'http://127.0.0.1:5000/prompt';
  
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt }), // Send the prompt in the request body
      });
  
      if (!response.ok) {
        throw new Error(`HTTP Error! Status: ${response.status}`);
      }
  
      const data = await response.json(); // Parse the response as JSON
      return data;
    } catch (err) {
      throw new Error(`Request Error: ${err.message}`);
    }
  };
  
  export default lawgpt;