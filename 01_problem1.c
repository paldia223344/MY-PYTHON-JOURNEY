 #include<stdio.h>
 
 int main(){
    // int age[4]=  {12, 24, 35, 57};

    // printf("Enter  all ages");
    //  for (int  i = 0; i < 5; i++)
    //  {
    //     printf(" enter ages  %d\n", age[i]);
    //  }

     
    //    for (int  i = 3; i >= 0; i--)
    //  {
    //     printf(" enter ages  %d\n", age[i]);
    //  }
     
     int arr[100],n;
      printf("Enter n:   ");
      scanf("%d\n", &n);
      int count = 0; 

    
     for (int i = 0; i <= n-1 ; i++)
     {
        if (i % 2 != 0)
       {
        printf("%d", i);
       }
      scanf("%d", &arr[i]);
       count += arr[i];  
       
     }
     
    

    return 0;
 }

// random function 