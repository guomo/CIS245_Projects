## Week 8 - Assigment 8.1
>This week we will create a program that performs file processing activities. Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory. Your program will prompt the user for the directory they would like to save the file in as well as the name of the file. The program should then prompt the user for their name, address, and phone number. Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user. 

>Once the data has been written your program should read the file you just wrote to the file system and display the file contents to the user for validation purposes. 

>Submit a link to your Github repository.

## Usage and Sample Output

```
(base) Oculus:~ gman$ python Assignment_8-1.py

What directory would you like to store you data? /tmp
Enter a filename to store your data: foo.txt
Enter your name: LeeLee Stone
Enter your address: 472 N Winchester Blvd.
Enter your phone #: 408-410-9898
Data saved...

/tmp/foo.txt contents are :


Gregory Stone, 506 S 3rd street, 408-410-9899
Karen Stone, 123 Main St, 702-321-5400
Linda Stone, 434 Braintree Ave., 306-443-8832
LeeLee Stone, 472 N Winchester Blvd., 408-410-9898
```