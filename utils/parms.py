class ModelParams:
    def __init__(self, prompt):
        self.params = {
            'prompt': prompt
        }

    def upsert_param(self, key, value):
        """Add a new parameter or update an existing one."""
        self.params[key] = value

    def remove_param(self, key):
        """Remove a parameter if it exists."""
        if key in self.params:
            del self.params[key]

    def __str__(self):
        """Custom string representation to print the parameters without braces."""
        params_list = [f"{key} = '{value}'" for key, value in self.params.items()]
        return ', '.join(params_list)
    
    def get_params(self):
        """Return the parameters dictionary."""
        return self.params