TOKEN = '1169806761:AAHxPcdXu8Bf1u7diD817AfeTlVAxsVo5NA'

def generate(emoji, text):
    text = list(text)
    emoji = str(emoji)
    a = ''
    text_result = ''
    for i in text:
        if i == ' ':
            text_result += '\n\n\n\n\n'

        elif i == 'А' or i == 'а':
            a += '⠀⠀⠀⠀{}\n'.format(emoji)
            a += '⠀⠀{}⠀⠀{}\n'.format(emoji, emoji)
            a += '{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji)
            a += '{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji)
            a += str(emoji) * 5 + '\n'
            a += '{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji)
            a += '{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji)
            a += '{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji)
            text_result += a + '\n'
            a = ''
        elif i == 'Б' or i == 'б':
            a += emoji * 4 + '\n'
            a += emoji + '\n'
            a += emoji + '\n'
            a += emoji * 4 + '\n'
            a += '{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji)
            a += '{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji)
            a += '{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji)
            a += emoji * 4 + '\n'
            text_result += a + '\n'
            a = ''
        elif i == 'В' or i == 'в':
            a += emoji * 3 + '\n'
            a += '{}⠀⠀⠀{}\n'.format(emoji, emoji)
            a += '{}⠀⠀⠀{}\n'.format(emoji, emoji)
            a += emoji * 4 + '\n'
            a += '{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji)
            a += '{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji)
            a += emoji * 4 + '\n'
            text_result += a + '\n'
            a = ''
        elif i == 'Г' or i == 'г':
            a += (emoji * 5) + '\n'
            a += (emoji) + '\n'
            a += (emoji) + '\n'
            a += (emoji) + '\n'
            a += (emoji) + '\n'
            a += (emoji) + '\n'
            a += (emoji) + '\n'
            a += (emoji + '\n')
            text_result += a + '\n'
            a = ''
        elif i == 'Д' or i == 'д':
            a += '⠀⠀{}\n'.format(emoji * 3)
            a += '⠀⠀{}⠀⠀{}\n'.format(emoji, emoji)
            a += '⠀⠀{}⠀⠀{}\n'.format(emoji, emoji)
            a += '⠀⠀{}⠀⠀{}\n'.format(emoji, emoji)
            a += emoji * 5 + '\n'
            a += '{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji)
            a += '{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji)
            text_result += a + '\n'
            a = ''
        elif i == 'Е' or i == 'е':
            a += emoji * 5 + '\n'
            a += emoji + '\n'
            a += emoji + '\n'
            a += emoji * 3 + '\n'
            a += emoji + '\n'
            a += emoji + '\n'
            a += emoji + '\n'
            a += emoji * 5 + '\n'
            text_result += a + '\n'
            a = ''
        elif i == 'Ж' or i == 'ж':
            a += '{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji)
            a += '{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji)
            a += '⠀⠀{}{}{}\n'.format(emoji, emoji, emoji)
            a += '  ⠀⠀{}\n'.format(emoji)
            a += '⠀⠀{}{}{}\n'.format(emoji, emoji, emoji)
            a += '{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji)
            a += '{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji)
            text_result += a + '\n'
            a = ''
        elif i == 'З' or i == 'з':
            a += ('⠀⠀{}{}{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('⠀⠀⠀⠀⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀  ⠀⠀{}{}\n'.format(emoji, emoji, emoji))
            a += ('⠀⠀⠀⠀⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('⠀⠀{}{}{}\n'.format(emoji, emoji, emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'Ы' or i == 'ы':
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}{}{}    {}\n'.format(emoji, emoji, emoji, emoji))
            a += ('{}⠀⠀⠀{}  {}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀⠀{}  {}\n'.format(emoji, emoji, emoji))
            a += ('{}{}{}    {} \n'.format(emoji, emoji, emoji, emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'И' or i == 'и':
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀{}{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}{}⠀⠀⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'К' or i == 'к':
            a += ('{}⠀⠀⠀⠀⠀⠀\n'.format(emoji))
            a += ('{}⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'Н' or i == 'н':
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += (emoji * 5 + '\n')
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'Л' or i == 'л':
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀{}⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'М' or i == 'м':
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}{} ⠀  {}{}\n'.format(emoji, emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'О' or i == 'о':
            a += ('⠀⠀{}{}{}⠀\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀⠀⠀ ⠀  {}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀   {}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀ ⠀  {}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀ ⠀  {}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀  ⠀ {}\n'.format(emoji, emoji))
            a += ('⠀⠀{}{}{}\n'.format(emoji, emoji, emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'п' or i == 'П':
            a += (emoji * 5 + '\n')
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'Й' or i == 'й':
            a += ('⠀⠀{}⠀⠀{}\n'.format(emoji, emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀{}{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}{}⠀⠀⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'Р' or i == 'р':
            a += (emoji * 4 + '\n')
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += (emoji * 4 + '\n')
            a += (emoji + '\n')
            a += (emoji + '\n')
            a += (emoji + '\n')
            text_result += a + '\n'
            a = ''
        elif i == 'Ч' or i == 'ч':
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += (emoji * 5 + '\n')
            a += ('⠀⠀⠀⠀⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀⠀⠀⠀⠀{}\n'.format(emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'С' or i == 'с':
            a += ('⠀⠀{}{}{}{}\n'.format(emoji, emoji, emoji, emoji))
            a += (emoji + '\n')
            a += (emoji + '\n')
            a += (emoji + '\n')
            a += (emoji + '\n')
            a += (emoji + '\n')
            a += ('⠀⠀{}{}{}{}\n'.format(emoji, emoji, emoji, emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'Т' or i == 'т':
            a += (emoji * 5 + '\n')
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'У' or i == 'у':
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += (emoji * 5 + '\n')
            a += ('⠀⠀⠀⠀⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀{}{}{}\n'.format(emoji, emoji, emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'Ю' or i == 'ю':
            a += ('{}⠀⠀{}{}{}\n'.format(emoji, emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}{}{}⠀⠀  {}\n'.format(emoji, emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀{}{}{}\n'.format(emoji, emoji, emoji, emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'Ф' or i == 'ф':
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += (emoji * 5 + '\n')
            a += ('{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += (emoji * 5 + '\n')
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'Я' or i == 'я':
            a += ('⠀⠀{}{}{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('⠀⠀{}{}{}\n'.format(emoji, emoji, emoji))
            a += ('⠀⠀⠀   {}{}\n'.format(emoji, emoji))
            a += ('⠀⠀ ⠀{}⠀{}\n'.format(emoji, emoji))
            a += ('⠀ ⠀{}⠀⠀{}\n'.format(emoji, emoji))
            a += ('⠀ {}⠀⠀⠀{}\n'.format(emoji, emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'ц' or i == 'Ц':
            a += ('{}⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += (emoji * 5 + '\n')
            a += ('⠀⠀⠀⠀⠀⠀⠀⠀{}\n'.format(emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'Ш' or i == 'ш':
            a += ('{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += (emoji * 5 + '\n')
            text_result += a + '\n'
            a = ''
        elif i == 'щ' or i == 'Щ':
            a += ('{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += ('{}⠀⠀{}⠀⠀{}\n'.format(emoji, emoji, emoji))
            a += (emoji * 5 + '\n')
            a += ('⠀⠀⠀⠀⠀⠀⠀⠀⠀{}\n'.format(emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'ь' or i == 'Ь':
            a = ''
            a += (emoji + '\n')
            a += (emoji + '\n')
            a += (emoji * 4 + '\n')
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += (emoji * 4)
            text_result += a + '\n'
            a = ''
        elif i == 'Х' or i == 'х':
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('⠀{}⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('⠀⠀{}⠀⠀{}\n'.format(emoji, emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀{}⠀⠀{}\n'.format(emoji, emoji))
            a += ('⠀{}⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('{}⠀⠀⠀⠀⠀⠀{}\n'.format(emoji, emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'Ъ' or i == 'ъ':
            a += ('{}{}\n'.format(emoji, emoji))
            a += ('⠀⠀{}\n'.format(emoji, emoji))
            a += ('⠀⠀{}\n'.format(emoji, emoji))
            a += ('⠀⠀{}{}{}\n'.format(emoji, emoji, emoji))
            a += ('⠀⠀{}⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('⠀⠀{}⠀⠀⠀{}\n'.format(emoji, emoji))
            a += ('⠀⠀{}{}{}\n'.format(emoji, emoji, emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'ї' or i == 'Ї':
            a += ('⠀⠀{}⠀⠀{}\n'.format(emoji, emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'І' or i == 'і':
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀{}\n'.format(emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'є' or i == 'Є':
            a += ('⠀⠀{}{}{}{}\n').format(emoji, emoji, emoji, emoji)
            a += (emoji + '\n')
            a += (emoji + '\n')
            a += (emoji * 3 + '\n')
            a += (emoji + '\n')
            a += (emoji + '\n')
            a += ('⠀⠀{}{}{}{}\n'.format(emoji, emoji, emoji, emoji))
            text_result += a + '\n'
            a = ''
        elif i == 'э' or i == 'Э':
            a += (emoji * 4 + '\n')
            a += ('⠀⠀⠀⠀⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀ {}{}{}\n'.format(emoji, emoji, emoji))
            a += ('⠀⠀⠀⠀⠀⠀⠀⠀{}\n'.format(emoji))
            a += ('⠀⠀⠀⠀⠀⠀⠀⠀{}\n'.format(emoji))
            a += (emoji * 4 + '\n')
            text_result += a + '\n'
            a = ''
        elif i == '?':
            a += ('⠀⠀{}{}{}\n').format(emoji,emoji,emoji)
            a += ("{}⠀⠀⠀⠀⠀⠀{}\n").format(emoji,emoji)
            a += ("{}⠀⠀⠀⠀⠀⠀{}\n").format(emoji, emoji)
            a += ("⠀⠀⠀⠀⠀⠀⠀⠀{}\n").format((emoji))
            a += ("⠀⠀⠀⠀⠀⠀{}\n").format(emoji)
            a += ("⠀⠀⠀⠀⠀⠀{}\n\n").format(emoji)
            a += ("⠀⠀⠀⠀⠀⠀{}\n").format(emoji)
            text_result += a + '\n'
            a = ''

        elif i == '!':
            a += ('{}\n').format(emoji)
            a += ('{}\n').format(emoji)
            a += ('{}\n').format(emoji)
            a += ('{}\n').format(emoji)
            a += ('{}\n').format(emoji)
            a += ('{}\n\n').format(emoji)
            a += ('{}\n').format(emoji)
            text_result += a + '\n'
            a = ''

        elif i == '.':
            a += ('{}{}\n').format(emoji,emoji)
            a += ('{}{}\n').format(emoji,emoji) 
            text_result += a + '\n'
            a = ''

        elif i == ',':
            a += ('{}{}\n').format(emoji,emoji)
            a += ('{}{}\n').format(emoji,emoji)
            a += ('⠀⠀{}\n').format(emoji)
            a += ('{}\n').format(emoji)
            text_result += a + '\n'
            a = ''

    return text_result