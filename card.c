#include <stdio.h>
#include <cs50.h>
#include <stdlib.h> // to use system

// Return Card Type (AMEX, Mastercard, Visa) from cardnumber.
// valid cc numbers for testing
// Amex - 378282246310005
// MC - 5404000000000001
// Visa - 4242424242424242

int main(void)
{

    long user_input;

    // Clear the screen
    system("clear");

    // prompt user for input
    do
    {
        user_input = get_long("Please enter you credit card number: ");
    }
    while(user_input < 0);


    /* validate with checksum if card is valid */

    // First check the len of the inputed card.
    int cclen = 0;
    long len_check = user_input;
    while(len_check != 0)
    {
        len_check=len_check/10;
        cclen++;
    }
    printf("len card is: %i \n", cclen);

    // Second Check if the length is 13, 15 or 16.
    if (cclen != 13 &&  cclen != 15 && cclen != 16)
    {
        printf("INVALID\n");
        return 0;
    }

    // Third perform LUN algoritm.
    int sum1 = 0;
    int sum2 = 0;
    long valid_check = user_input;
    int tmpsum = 0;
    int digit1 = 0;
    int digit2 = 0;

    do
    {
        // take the last digit
        sum1 += valid_check % 10;
        valid_check=valid_check/10;
        //printf("num... %i \n", sum1);

        // take second last digit
        tmpsum = valid_check % 10;
        printf("tmpsum... %i \n", tmpsum);
        valid_check = valid_check/10;
        tmpsum = tmpsum * 2;
        digit1 = tmpsum % 10;
        digit2 = tmpsum / 10;
        sum2 = sum2 + digit1 + digit2;
        printf("sum2... %i \n", sum2);
    }
    while (valid_check  > 0);

    printf("sum 1 : %i \n", sum1);
    printf("sum 2 : %i \n", sum2);

    // Card not valid if sum1 + sum2 % 10 != 0
    int total = 0;
    total = sum1 + sum2;
    printf("total %i \n", total);

    if (total % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    // Get the last two numbers..
    long count = user_input;
    //printf("first_two : %i \n", first_two);

    do
    {
        count = count / 10;

    }
    while (count > 100);
    int first_two = count;


    // Print out card type...
    if (first_two == 34 || first_two == 37) {
        printf("AMEX\n");
    }
    else if (first_two == 51 || first_two == 52 || first_two == 53 || first_two == 54 || first_two == 55) {
        printf("MASTERCARD\n");
    }
    else if (first_two / 10 == 4) {
        printf("VISA\n");
    }
    else {
        printf("INVALID\n");
        }

    //Inform computer program is done.
    return 0;
}




