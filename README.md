Cooking assistant using langgraph.

**To run in Docker:**

Build the Docker image:
```bash
docker build -t langgraph-cooking-assistant .
```
Run the Docker container with your Google API key:
```bash
docker run -it --rm -e GOOGLE_API_KEY="your_actual_google_api_key" langgraph-cooking-assistant
```
