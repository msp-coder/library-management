
books = {'a':10,'b':4,'c':5,'d':7}
user = {'user':'xyz','phone':6374643577,'no_of_books':1,'books_taken':['a']}

def display_books():
    for i,j in books.items():
        print(f'{i}    {j}')
        

def user_details():
    print('user:',user['user'])
    print('phone:',user['phone'])
    print('no_of_books:',user['no_of_books'])
    print('books_taken',user['books_taken'])
    
    no = user['no_of_books']
    if no == 0:
        print('you did not borrow any books')
    else:
        print('no of books taken is :', no )
        


def borrow_book():
    if user['no_of_books']>=3:
        print('can not borrow ur limit is over')
    else:
        n = input('which book u want:')
        if n in books.keys():
            if books[n]>0:
                if n in user['books_taken']:   
                    print('This book already taken so cannot take another book in same author')
                else:
                    books[n]=books[n]-1
                    user['no_of_books']=user['no_of_books']+1
                    user['books_taken'].append(n)
                    print('sucessfully borrowed')
                                
            else:
                print('Author not gettig any books')       
        else:
            print('This author is not available')
 
def return_book():
    if user['no_of_books'] == 0:
        print('can not return because ur not taken books')
    else:
        r = input('which book u return:')
        if r in books.keys():
            if r in user['books_taken']:
                books[r]=books[r]+1
                user['books_taken'].remove(r)
                user['no_of_books']=user['no_of_books']-1
                print('sucessfully return')
            else:
                print('This author book is not taken')     
        else:
            print('can not return because this author not present in library')

def exit_library():
    print('to exit')


def main():
    print('press 1: Dispaly all books in library')
    print('press 2: User details in library')
    print('press 3: Borrow books in library')
    print('press 4: Return books in library')
    print('press 5: To exit library')
    print('---------------------------------')
    
    i = int(input('enter a number:'))
    if i == 1:
        display_books()
        print('------------------------')
        main()
    elif i == 2:
        user_details()
        print('------------------------')
        main()
    elif i == 3:
        borrow_book()
        print('------------------------')
        main()
    elif i == 4:
        return_book()
        print('------------------------')
        main()
    elif i == 5:
        exit_library()
        print('------------------------')
        main()

        
main()

        
        
        
                 
                
                


                
            

         
        
            
            
        
    
    

        

        




display_books()
print('---------------------------------------')
user_details()
borrow_book()
    
