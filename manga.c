#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct manga
{
  char manganame[30];
  char artist[30];
  int pages;
  float price;
};

int main()
{
  struct manga store[100];
  char artistname[30], manganame[30];
  int i, noofmanga, count;
  i = 0;
  noofmanga = 0; 
  count = 0;

  while (noofmanga != 6)
  {
     printf("\n****************Manga Management System***************\n");
    printf("\n\n1. Store manga information\n2. Show manga information\n");
    printf("3. Display all the manga\n");
    printf("4. List the title of manga\n");
    printf("5. List the number of manga stored in database\n");
    printf("6. Exit");

    printf("\n\nEnter one option from above: ");
    scanf("%d", &noofmanga);

    switch (noofmanga)
    {
    /* Add book */
    case 1:

      printf("Enter Manga name = ");
      scanf("%s", store[i].manganame);

      printf("Enter artist name = ");
      scanf("%s", store[i].artist);

      printf("Enter pages = ");
      scanf("%d", &store[i].pages);

      printf("Enter price = ");
      scanf("%f", &store[i].price);
      count++;

      break;
    case 2:
      printf("you have entered the following information\n");
      for (i = 0; i < count; i++)
      {
        printf("Manga name = %s", store[i].manganame);

        printf("\t artist name = %s", store[i].artist);

        printf("\t  pages = %d", store[i].pages);

        printf("\t  price = %f", store[i].price);
      }
      break;

    case 3:
      printf("Enter author name : ");
      scanf("%s", artistname);
      for (i = 0; i < count; i++)
      {
        if (strcmp(artistname, store[i].artist) == 0)
          printf("%s %s %d %f", store[i].manganame, store[i].artist, store[i].pages, store[i].price);
      }
      break;

    case 4:
      printf("Enter manga name : ");
      scanf("%s", manganame);
      for (i = 0; i < count; i++)
      {
        if (strcmp(manganame, store[i].manganame) == 0)
          printf("%s \t %s \t %d \t %f", store[i].manganame, store[i].artist, store[i].pages, store[i].price);
      }
      break;

    case 5:
      printf("\n No of manga in library : %d", count);
      break;
    case 6:
      exit(0);
    }
  }
  return 0;
}
