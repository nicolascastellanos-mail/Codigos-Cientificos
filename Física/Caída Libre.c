#include <stdio.h>
#include <stdlib.h>

/*
g is the gravity in meters per second squared
i is the initial height in meters
t is the time in seconds
h is the current height in meters
s is the speed in meters per second
*/

int main()
{
	double g;
	double i;
	double t;
	double h;
	double s;
	
	g = 3;
	i = 1000;
	t = 0;
	h = 0;
	s = 0;
	
	while(h >= 0)
	{
		system("cls");
		printf("Time     %lf\n", t);
		printf("Height   %lf\n", h);
		printf("Speed    %lf\n", s);

		// sleep(1);
	
		t += 1;
		h = i - (0.5 * g * (t*t));
		s = g * t;
	}
	
	if(h != 0)
	{
		system("cls");
		printf("Time     %lf\n", t);
		printf("Height   %lf\n", h);
		printf("Speed    %lf\n", s);

		// sleep(1);
	
		t += 1;
		h = i - (0.5 * g * (t*t));
		s = g * t;
	}
	
	return 0;
}
