text = "hello world"

try:
    # Attempt to call a non-existent method
    # Python strings have 'upper()', not 'toUpperCase()'
    print(text.toUpperCase())
except AttributeError as e:
    # Handle the error gracefully
    print(f"Error caught: {e}")
    print("Suggestion: Use 'text.upper()' instead.")