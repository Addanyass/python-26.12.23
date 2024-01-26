#zad1
# user_text = "как дела. когда идем гулять. погода сегодня хорошая"
# user_razdel = user_text.split(".")

# capitalized_sentences = [userA.strip().capitalize() for userA in user_razdel if userA]       #в каждое предложение начинается с большой буквы 
# user_Nk = ". ".join(capitalized_sentences)                                                   #объеденения элементов списка по точке , конечный результат уже строка (был списком и в квадратных скобках)
# print(user_Nk)
 

# import string
# user_text = "как дела! когда идем гулять? погода сегодня хорошая/"
# count_punctuation = 0
# for eda in user_text:
#     if eda in string.punctuation:  #считываем сколько любых восклицательных и пунктуационных знаков в тексте
#         count_punctuation += 1
# print(count_punctuation)        
#-----------------------------------------------------------------------------------------------------------


#zad2

# input_list = input("введите элементы списка через пробел").split() #ввод цифр и разделение их по пробелу и в запись  их в список 
# input_list = [int(x) for x in input_list] #тут числовой тип данных , а не просто строки 
# number_to_find = int(input("введите число,которое вам нужно найти:"))
# count = input_list.count(number_to_find)     #считает кол-во сколько раз встречается одно и тоже число в списке
# print(count)

#----------------------------------------------------------------------------------------------------------------

#zad3

# input_list = input("введите элементы списка через пробел").split() #ввод цифр и разделение их по пробелу и в запись их в список 
# input_list = [int(x) for x in input_list]
# sum_vseh_elementov = sum(input_list)                                #sum(функц вычесляющая сумму всех чисел)
# average = sum_vseh_elementov / len(input_list)                      #нахождение средней арифмет чисел sum/ len(сколько элементов в списке)
# print(average)
