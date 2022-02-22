def main():
    word = 'ChiCliete'
    print(faca_minusculo(word))
    
    
    
def faca_minusculo(word):
    minusculo = ''
    for char in word:
        if 'A' <= char <= 'Z':
            char = chr(ord(char) + (ord('a') - ord('A')))
            
        minusculo +=char
    
    return minusculo


main()