a_list = ['.com', 'bobby', '.com', 'hadz', '.com']

new_list = [item if item != '.com' else '.abc'
        for item in a_list]

# 👇️ ['.abc', 'bobby', '.abc', 'hadz', '.abc']
print(new_list)
