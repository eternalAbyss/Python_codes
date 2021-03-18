num = int(float(input('Enter a number: ')))
print('hello ' * num)

# try: 
#     x = int(input('Enter a number: '))
# except ValueError:
#     print("The Error is ValueError!")
# except KeyboardInterrupt:
#     print('Interrupted using the keyboard!')
# finally:
#     print("Attempted Input!\n")

try: 
    x = int(input('Enter a number: '))
except Exception as e:
    print('The Error is {}!'.format(e))
finally:
    print("Attempted Input!\n")

