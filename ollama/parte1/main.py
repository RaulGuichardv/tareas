import ollama

# Use the generate function for a one-off prompt
result = ollama.generate(model='gemma3:4b', prompt='por que el cielo es azul?')
print(result['response'])