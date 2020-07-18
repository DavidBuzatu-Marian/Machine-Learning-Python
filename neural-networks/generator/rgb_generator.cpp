#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <fstream>

std::ofstream g("out.txt");

void print_text_color(int red_c, int green_c, int blue_c)
{
    int text_color = 0;
    // credits to https://stackoverflow.com/a/1855903/11023871 for formula

    double luminance = (0.299 * red_c + 0.587 * green_c + 0.144 * blue_c) / 255;
    if (luminance > 0.5)
    {
        text_color = 0; // dark
    }
    else
    {
        text_color = 1; // white
    }
    g << red_c << ", " << green_c << ", " << blue_c << ", " << text_color << "\n";
}

int main()
{

    srand(time(NULL));
    for (int i = 0; i < 10000; ++i)
    {
        print_text_color(rand() % 255, rand() % 255, rand() % 255);
    }
    return 0;
}