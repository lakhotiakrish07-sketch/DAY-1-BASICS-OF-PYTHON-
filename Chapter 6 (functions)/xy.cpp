#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));              // seed for random number
    int secret = rand() % 100 + 1; // random number between 1 and 100
    int guess;
    int attempts = 0;

    cout << "Guess the number (1 to 100)\n";

    do {
        cout << "Enter your guess: ";
        cin >> guess;
        attempts++;

        if (guess > secret) {
            cout << "Too high!\n";
        } else if (guess < secret) {
            cout << "Too low!\n";
        } else {
            cout << "Correct! 🎉\n";
            cout << "Attempts taken: " << attempts << endl;
        }
    } while (guess != secret);

    return 0;
}
