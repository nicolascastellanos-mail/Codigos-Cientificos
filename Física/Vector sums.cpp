// 3/8/2022 2:03 PM EST

#include <iostream>
#include <cmath>
#include <vector>
#include <string>

class PhysicsVector
{
private:
	std::string name;
	float magnitude;
	float direction;
	float angle;
	float xCoord;
	float yCoord;

public:
	PhysicsVector(std::string name)
	{
		this -> name = name;
		this -> magnitude = 0;
		this -> direction = 0;
		this -> angle = 0;
		this -> xCoord = 0;
		this -> yCoord = 0;
	}
	
	PhysicsVector(std::string name, float magnitude, float direction)
	{
		this -> name = name;
		this -> magnitude = magnitude;
		this -> direction = direction;
		calculateCoords();
	}
	
	PhysicsVector(std::string name, float xCoord, float yCoord, int any)
	{
		this -> name = name;
		this -> xCoord = xCoord;
		this -> yCoord = yCoord;
	}

	void calculateCoords()
	{
		this -> angle = this -> direction;
		
		if (direction > 90 && direction < 180)
		{
			this -> angle -= 90;
		}else if (direction > 180 && direction < 270)
		{
			this -> angle -= 180;
		}else if (direction > 270 && direction < 360)
		{
			this -> angle -= 270;
		}
		
		this -> angle *= (M_PI / 180);

		if (this -> direction == 0)
		{
			this -> xCoord = this -> magnitude;
			this -> yCoord = 0;
		}else if (direction == 90)
		{
			this -> xCoord = 0;
			this -> yCoord = this -> magnitude;
		}else if (direction == 180)
		{
			this -> xCoord = this -> magnitude * -1;
			this -> yCoord = 0;
		}else if (direction == 270)
		{
			this -> xCoord = 0;
			this -> yCoord = this -> magnitude * -1;
		}else if (direction > 0 && direction < 90)
		{
			this -> xCoord = (this -> magnitude * cos(this -> angle));
			this -> yCoord = (this -> magnitude * sin(this -> angle));
		}else if (direction > 90 && direction < 180)
		{
			this -> xCoord = (this -> magnitude * sin(this -> angle)) * -1;
			this -> yCoord = (this -> magnitude * cos(this -> angle));
		}else if (direction > 180 && direction < 270)
		{
			this -> xCoord = (this -> magnitude * cos(this -> angle)) * -1;
			this -> yCoord = (this -> magnitude * sin(this -> angle)) * -1;
		}else if (direction > 270 && direction < 360)
		{
			this -> xCoord = (this -> magnitude * sin(this -> angle));
			this -> yCoord = (this -> magnitude * cos(this -> angle)) * -1;
		}
	}
	
	void describe()
	{
		std::cout << "Name: " << this -> name << std::endl;
		std::cout << "Magnitude: " << this -> magnitude << std::endl;
		std::cout << "Direction: " << this -> direction << std::endl;
		std::cout << "Position in x: " << this -> xCoord << std::endl;
		std::cout << "Position in y: " << this -> yCoord << std::endl;
	}
	
	void edit(std::string name, float magnitude, float direction)
	{
		this -> name = name;
		this -> magnitude = magnitude;
		this -> direction = direction;
		calculateCoords();
	}
	
	void sumVector(PhysicsVector anotherVector)
	{
		this -> xCoord += anotherVector.xCoord;
		this -> yCoord += anotherVector.yCoord;
		this -> magnitude = sqrt((xCoord * xCoord) + (yCoord * yCoord));
		
		if (this -> xCoord > 0 && yCoord == 0)
		{
			this -> direction = 0;
		}else if (this -> xCoord == 0 && this -> yCoord > 0)
		{
			this -> direction = 90;
		}else if (this -> xCoord < 0 && this -> yCoord == 0)
		{
			this -> direction = 180;
		}else if (this -> xCoord == 0 && this -> yCoord < 0)
		{
			this -> direction = 270;
		}

		if (this -> xCoord > 0 && this -> yCoord > 0)
		{
			this -> direction = atan(yCoord / xCoord) * 180 / M_PI;
		}else if (this -> xCoord < 0 && this -> yCoord > 0)
		{
			this -> direction = atan(xCoord / yCoord) * 180 / M_PI;
		}else if (this -> xCoord < 0 && this -> yCoord < 0)
		{
			this -> direction = atan(yCoord / xCoord) * 180 / M_PI;
		}else if (this -> xCoord > 0 && this -> yCoord < 0)
		{
			this -> direction = atan(xCoord / yCoord) * 180 / M_PI;
		}
	}
};

int main(int argc, char const *argv[])
{
	std::vector<PhysicsVector> createdVectors;
	PhysicsVector newVector("VOID");
	PhysicsVector resultVector("SUM");

	std::string name;
	float magnitude;
	float direction;
	
	int counter = 0;

	std::cout << "Name of the new vector: ";
	std::cin >> name;
	std::cout << "Magnitude of the new vector: ";
	std::cin >> magnitude;
	std::cout << "Direction of the new vector: ";
	std::cin >> direction;
	newVector.edit(name, magnitude, direction);
	createdVectors.push_back(newVector);

	while (true)
	{
		system("cls");
		
		std::cout << std::endl << "Created vectors:" << std::endl;
		
		counter = 0;
		
		while (counter < createdVectors.size())
		{
			std::cout << std::endl;
			createdVectors.at(counter).describe();
			std::cout << std::endl;
			counter += 1;
		}
		
		if (counter > 1)
		{
			std::cout << "Name of the new vector (\"SUM\" to sum all vectors): ";
		}else
		{
			std::cout << "Name of the new vector: ";
		}

		std::cin >> name;

		if (name == "SUM")
		{
			counter = 0;

			while (counter < createdVectors.size())
			{
				resultVector.sumVector(createdVectors.at(counter));
				counter += 1;
			}

			break;
		}

		std::cout << "Magnitude of the new vector: ";
		std::cin >> magnitude;
		std::cout << "Direction of the new vector: ";
		std::cin >> direction;
		newVector.edit(name, magnitude, direction);
		createdVectors.push_back(newVector);
	}

	std::cout << std::endl;
	resultVector.describe();
	
	system("pause");
}

// 3/8/2022 3:49 PM EST - All I have to do is to sum the vectors and calculate the resultant vector
// 3/8/2022 3:54 PM EST - Starting to finish job
// 3/8/2022 5:27 PM EST
