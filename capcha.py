from captcha.image import ImageCaptcha
import random
#-------------------------------------------------------------------------------
image = ImageCaptcha(width = 280, height = 90)

characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I',
'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1',
'2','3','4','5','6','7','8','9','0','_']

counter = 1
holder = ''
name_file = ''
print(len(characters))
for j in range(100):
    while counter <= 6:
        if counter > 6:
            counter = 1
            holder = ''
            captcha_text = ''
            name_file = ''
        else:
            random_choice = random.choice(characters)
            print(counter, ":" ,random_choice)
            counter += 1
            holder += random_choice

            print("New Created Captcha:", holder)
            print("-------------------------")
        print("This Name for Your File:",name_file)
        
        captcha_text = holder
        name_file = holder + '.png'
        data = image.generate(captcha_text)
        image.write(captcha_text, name_file)
