# kb-layout-converter-english
A small python script to convert a text in english into such a gibberish that the characters correspond to the keys you would need to type if you were to type it in another keyboard layout that you want to get the feel of typing in, without having to learn it. Only for 105-keys (ISO) keyboards.

# Why use this
Well, if you have pain when typing and want to see if another layout can help you feel less pain when typing, (first of all, ask your doctor) then you can use this script to convert text to type it using the same keys you would use if you were using another keyboard layout. There are keyboard layouts like Dvorak, Colemak, and Workman, among others, that were designed to try to be more ergonomic than Qwerty-based layouts (usually, the ones computers sold in english speaking countries use)

# How to use
You need to have both files: layout-converter.py and layouts.txt in a directory you have permissions to write to (because the text-converted.txt file will be written there)
Run the script like this:
python3 layout-converter.py your_input_file
then the script will create, or overwrite, a file named converted-text.txt
Now you just have to open the converted-text.txt and open another editor window to copy the text, so that you can get the feel of typing it the layout you wanted to taste.

# How to edit the layouts.txt file
The layouts.txt file has some popular keyboard layouts for english in it, but you can edit it to add your own layout for english if it isn't there (you can only add levels 1 and 2, level 2 is the shifted symbols). The format for each line in the  layouts.txt file is:
<layout_name> <tabs> <characters for each row of the layout, (using this character 'º' to represent the key that is right next to the right of the left shift), and then the same characters using the shift key (level 2) (using this character '²' to represent the key that is right next to the right of the left shift, the infamous LSGT key plus shift)>

(if your layout has dead keys, then you have to press that key twice ,or press the key and then space, in order to produce a version of the character that you can add to your custom layout in the layouts.txt file.)
