is_magician = True
is_expert = True

# check if magician and expert : print 'you are a master magician'
if is_magician and is_expert:
    print('you are a master magician')
elif is_magician:
    print('at least you are getting there')
else:
    print('you need magic powers')
# check if magician but not expert : print 'at least you're getting there'
# check if not a magician : print 'you need magic powers'

is_expert = False

if is_magician and is_expert:
    print('you are a master magician')
elif is_magician:
    print('at least you are getting there')
else:
    print('you need magic powers')

is_magician = False

if is_magician and is_expert:
    print('you are a master magician')
elif is_magician:
    print('at least you are getting there')
else:
    print('you need magic powers')