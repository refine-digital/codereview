# File: modules/agent_logic.py
# Version: 1.0.0

def query_agent(connection, model_name, system_prompt, context, task_prompt):
    """Sends a request to the appropriate model using the correct connection."""
    try:
        response = connection.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"{task_prompt}\n\n--- CONTEXT ---\n{context}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error querying model '{model_name}': {e}"

def get_agent_for_file(ext):
    """Selects the agent name based on file extension."""
    if ext == 'php':
        return 'php_reviewer'
    if ext == 'sql':
        return 'mysql_reviewer'
    # Add other mappings here
    return 'project_lead'

