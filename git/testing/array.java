import java.util.Arrays;
class Array{
	public static void main(String[] args) {
		 //int[] arr=new int [];
		 int[] arr={2,3,52,5,6,7,4,90,10};
		 //int c=max(arr);
		 //System.out.println(c);
		 //selectionsort(arr);
		 maopao(arr);
	}

	//xuanze paixu
	/*public static  void  selectionsort(int[] arr1)
	{
		
		for (int i=arr1.length-1;i>0; i--) 
		{
			int maxindex=0;
			int max=arr1[0];
			 //find the miximum in the arr1[]  2,3,52,5,6,7,4,90,10
			for (int j=0;j<=i ;j++ ) 
			{
				if (arr1[j]>arr1[maxindex]) 
				{
				maxindex=j;
				max=arr1[maxindex];
				System.out.println(maxindex );
 				}
			}
			//swap  the maximum to the last
			if (maxindex!=i) {
				arr1[maxindex]=arr1[i];
				arr1[i]=max;
				System.out.println("arr["+i+"]="+arr1[i]);
			}
			//u can't print it in this way!!!!!!!!!!!
			//System.out.println(arr1)
			System.out.println(Arrays.toString(arr1));
		}
		System.out.println(Arrays.toString(arr1));
	}*/


	//the max  one in array
	/*public static int   max (int[] arr1)      
	{
		int m;
		m=arr1[0];
		for (int i=0;i<9 ;i++ ) {
			if (arr1[i]>m) {
				m=arr1[i];
			}
		}
			return m;
		
	}*/

	//maopao paixu
	public static void maopao(int[] arr1)
	{
		for (int j=arr1.length-1;j>=0 ;j-- ) {
			for (int i=0;i<j ;i++ ) {
				int a;
				if (arr1[i]>arr1[i+1]) {
					a=arr1[i+1];
					arr1[i+1]=arr1[i];
					arr1[i]=a;
				}
			}
			
		}
		System.out.println(Arrays.toString(arr1));
	}



}



