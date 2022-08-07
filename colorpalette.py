#Note: The program has been organized into functions. It doesn't contain any global variables. The main function is what calls all the programs and print statements sequentially. Since it only contains functions, I didn't see the need to create additional files.

#Notes about RGB:
#In the RGB way of color coding, the higher the numbers, the lighter the corresponding colors

import picture 

def extract_and_standardize_colors(image,width,height,pixels_list,rgb_val):
  #this function will loop through the image to extract the colors from each pixel and standardize them so they're stored correctly in the dictionary

  for y in range(height): #this will loop from 0 to the height of the image
      for x in range(width): #this will loop from 0 to the width of the image
        #get the red, green, and blue values of each pixel and store them as a string
        red=str(picture.get_red(image,x,y))
        green=str(picture.get_green(image,x,y))
        blue=str(picture.get_blue(image,x,y))

        #this will make sure each RED value consits of 3 digits, for example a red value of "35" would be converted to R "035"
        if len(red)==1:
          red=str(0)+str(0)+red
        elif len(red)==2:
          red=str(0)+red
        else:
          red=red

        #this will make sure each GREEN value consits of 3 digits, for example G 35 would be converted to G 035
        if len(green)==1:
          green=str(0)+str(0)+green
        elif len(green)==2:
          green=str(0)+green
        else:
          green=green

        #this will make sure each BLUE value consits of 3 digits, for example B 35 would be converted to B 035
        if len(blue)==1:
          blue=str(0)+str(0)+blue
        elif len(red)==2:
          blue=str(0)+blue
        else:
          blue=blue

        #concatenate the RGB values in a string and store it in a variable
        #this will store the RGB values collectively in a string for eg. as "035035035"
        rgb_val=red+green+blue

        #add standardization store this RGB value in an empty list
        pixels_list.append(rgb_val)

def add_rgb_val(rgbcolor,line_number,pixel_dict):
  #This function handles the work of recording that a given RGB value (rgbcolor) was found on the given line_number in the dictionary pixel_dict

  #This function draws on the function from Lab 4 - Concatenation which records the line numbers on which a certain word occurs. The dictionary that this function produces isn't particuarly useful for the program itself. Therefore, the functions ahead use the values of the dictionary as a foundation - they do this by counting the line numbers for each color to compute the no. of occurences for each color.

  #pixel_dict will be stored as a dictionary, where the keys are rgbcolors (i.e., strings) and the values are lists of line numbers.

  list_of_line_numbers=[]
  if rgbcolor!="":
    if rgbcolor in pixel_dict: #if the color is in the dictionary
      pixel_dict[rgbcolor].append(line_number) #in the entry for the color add the line number
    else: #if the color is not in the dictionary
      list_of_line_numbers.append(line_number)
      pixel_dict[rgbcolor]=list_of_line_numbers
  #print(pixel_dict[rgbcolor])
  #print(pixel_dict) #this was used as a check while writing the program. if pixel_dict is printed at this stage, it is  extremely lengthy and isn't very useful. pixel_dict will be modified into a more intuitive dictionary further
  return pixel_dict

def count_occurences(color,pixel_dict):
  #This functions modifies the pixel dictionary. As of now, pixel_dict stores line numbers, thus this function will overwrite the line number entries with their sum. Their sum will be equal to number of occurences of each pixel color. 
  
  #pixel_dict is the dictionary storing the pixel_dict, so pixel_dict[color] should be sum of the occurences of that particular color

  output=""
  for keys in sorted(pixel_dict.keys()): #each key is the color
    output=output+keys
    counter=0
    for each_value in pixel_dict[keys]:
      counter=counter+1
    pixel_dict[keys]=counter
    #print(output,"",counter)
    #print(pixel_dict[keys])
    output=""
  return output

def find_colors(word,pixel_dict,top_colors):
  #this function will loop through the entire dictionary to find the top 5 most occuring colors 
  first_color=0
  second_color=0
  third_color=0
  fourth_color=0
  fifth_color=0
  temp=0
  current_value=0


  for color in sorted(pixel_dict.keys()): #each key is the color
    current_value=int(pixel_dict[color])
    #print("this is current value",current_value)
    #temp=current_value #temp will store the value of the previous color
    #print("this is temp value",temp)
    if int(current_value)>int(temp):
      first_color=color #this would be 255244233 for eg.
      #print("this is the first color",first_color)
      temp=current_value
    else:
      temp=temp
  temp=0
  top_colors.append(first_color)
  #the following line of code will overwrite the value for the first color in the dictionary so that the next time we loop through the dictionary to find the second color, it doesn't pick up this one
  pixel_dict[first_color]=int(0)

  for color in sorted(pixel_dict.keys()): #each key is the color
    #print("pixel dict val",pixel_dict[color])
    current_value=int(pixel_dict[color])
    #print("current value is",current_value)
    #print("this is temp",temp)
    if int(current_value)>int(temp):
      second_color=color
      temp=current_value
    else:
      temp=temp
  temp=0
  top_colors.append(second_color)
  pixel_dict[second_color]=int(0)

  for color in sorted(pixel_dict.keys()): #each key is the color
    current_value=pixel_dict[color]
    if int(current_value)>int(temp):
      third_color=color
      temp=current_value
    else:
      temp=temp
  temp=0
  top_colors.append(third_color)
  pixel_dict[third_color]=int(0)
  
  for color in sorted(pixel_dict.keys()): #each key is the color
    current_value=pixel_dict[color]
    if int(current_value)>int(temp):
      fourth_color=color
      temp=current_value
    else:
      temp=temp
  temp=0
  top_colors.append(fourth_color)
  pixel_dict[fourth_color]=int(0)

  for color in sorted(pixel_dict.keys()): #each key is the color
    current_value=pixel_dict[color]
    if int(current_value)>int(temp):
      fifth_color=color
      temp=current_value
    else:
      temp=temp
  temp=0
  top_colors.append(fifth_color)
  pixel_dict[fifth_color]=int(0)
  #print(pixel_dict)
  #print(top_colors)
  return top_colors

def palette_graphic(list_of_top_colors,palettewidth,paletteheight,paletteimage):
  #this function uses the picture module to create a graphical representation of the color palette - it  displays the top 5 colors in the image in horizontal bars

  for i in range(5):
    allcolorvalues=list_of_top_colors[i] #allcolorvalues will store the RGB of the corresponding color from the list
    #allcolorvalues is a string
    red=allcolorvalues[0:3] #'234'#splicing the string to extract the RED component of the value
    green=allcolorvalues[3:6] #string splicing for the green value
    blue=allcolorvalues[6:9] #string splicing for the blue value

    red=int(red) #converts the RED string into an integer
    blue=int(blue)
    green=int(green)

    #the following part will set the colors for each of the pixels
    for pixelheight in range(50*i,50+(50*i)): #this range ensures that each color takes up a fifth of the image
      for pixelrow in range(palettewidth):
        picture.set_red(paletteimage,pixelrow,pixelheight,red)
        picture.set_green(paletteimage,pixelrow,pixelheight,green)
        picture.set_blue(paletteimage,pixelrow,pixelheight,blue)

  return paletteimage

def main():

  print("Welcome to the Color Palette Generator!")

  filename=input(print("Please enter a filename: "))
  #filename="test1.png"

  print("Please wait a moment for the color palette to display")

  try:
    #Loading the image
    image = picture.load_image(filename)
    #Stores the dimensions of the image
    width = picture.image_width(image)
    height = picture.image_height(image)

    #creates an empty list to store the RGB values of each pixel
    pixels_list=[] 

    #this variable will store the combined rgb value - suppose a color has 255 RED 200 GREEN AND 100 BLUE, it will store this as rgb_val=255200100 thus it will be a string
    rgb_val=""  

    #this function will loop through the image to extract the colors from each pixel and standardize them so they're stored correctly in the dictionary
    extract_and_standardize_colors(image,width,height,pixels_list,rgb_val)

    #creates an empty dictionary where the keys are the colors in the form of RGB value strings and the elements are their sum of occurences in the image
    pixel_dict={}

    #list of 5 strings that represent the top-5 colors in the image
    top_colors=[]

    #Reads the list by looping through one line at a time and then calls the add_rgb_val function to add the color to the pixel dictionary
    for pixels_list_index in range(0,len(pixels_list)):
      word=pixels_list[pixels_list_index]
      add_rgb_val(word,pixels_list_index,pixel_dict)

    #Calls the count_occurences function
    count_occurences(word,pixel_dict) 

    #creates a list "top_colors" to store the top 5 colors as found from the find_colors function
    top_colors = find_colors(word,pixel_dict,top_colors)

    #creates a new list to store the values of top_colors - this is a duplicate list essentially
    list_of_top_colors=top_colors

    #defines the dimensions of the blank image for the color palette
    palettewidth=250
    paletteheight=250
    paletteimage = picture.blank_image(palettewidth,paletteheight)
    #calls the palette_graphic function that sets the colors for each pixel in the color palette image
    palette_graphic(list_of_top_colors,palettewidth,paletteheight,paletteimage)

    #draws and displays the output
    picture.new_picture(palettewidth, paletteheight)
    picture.draw_image(0,0,paletteimage)
    picture.run()
    
  except:
    print("Error - File does not exist!")
    return
  
main()

