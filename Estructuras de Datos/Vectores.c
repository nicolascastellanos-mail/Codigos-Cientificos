// 11/01/2022 8:50 p.m

#include <iostream>
#include <vector>
#include <string>

int main(int argc, char const *argv[])
{
	std::vector<std::string> nameList;
	std::string enteredName;
	char userChoose;

	do
	{
		std::cout << "Please, enter a name: ";
		std::cin >> enteredName;
		nameList.push_back(enteredName);
		std::cout << "Do you want to add another name? Y/n: ";
		std::cin >> userChoose;
	} while (userChoose == "Y");

	std::cout << "The names on the list are:" << std::endl;

	for (int i = 0; i <= nameList.size(); ++i)
	{
		std::cout << i << ". " << nameList[i] << std::endl;
	}

	return 0;
}

// I made this only viewing the definition and the adding of a element of a vector class instance. I didn't knew vector and string
// classes before. I am annoyed because it is on the std namespace, I don't even know why. The .size() was learnt from the array
// class, which I didn't knew too, but I just viewed it, but I used vectors to "make the list unlimited"

// 11/01/2022 9:12 p.m
