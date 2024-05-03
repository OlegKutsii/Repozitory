def total_salary (filename):
    with open(filename, 'r', encoding='utf-8') as text:
        data = text.read()
        n = ''
        new_text = []    
        for word in data:
            if '0' <= word <= '9':
                n += word
            else:
                if n != '':
                    new_text.append(int(n))
                    n = ''        
        if n !='':
            new_text.append(int(n))
    total = sum(new_text)
    average = sum(new_text)//len(new_text)
    return total, average

    
