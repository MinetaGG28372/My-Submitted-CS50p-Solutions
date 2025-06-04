#Here's my solution using natural thought process, not covering weird cases

random_text = input("Give out the script at normal speed: ")
    #the user would enter the desired lines, where " " shall be replaced with "..."
result = random_text.replace(" ", "...")
     #we use the replace method to replace blank occurences with the low dots. Third argument is unspecificed so ALL blank occurences would be replaced.
     #The result might not be desirable if we put ... at either ends of the input
     # I haven't figured out how that issue should be tackled.
print("The slowed-down version is: ",result)
    #Give the result out of the screen
