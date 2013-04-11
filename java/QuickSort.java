/*// divide & conquier with pivot values 

1. Class QuickSort 
	- properties (array, length)
	- sort
		- check for nulls & zeros
		- call quicksort (0, length-1)
	- quicksort 
		- get pivot value
		- divide the lists
			- find element to swap
			- swap them
			- go until left passes right
		- recursion call until right passes low & left passes high
	- swap

*/




// divide & conquer using pivot value

public class QuickSort(){

	int[] numbers;
	int length;

	public void sort(int[] values){
		// check for nulls
		if (values == null || values.length == 0)
			return;
		// delegate to quicksort
		this.numbers = values;
		length = values.length;
		quicksort (0, length-1); 
	}

	public void quicksort(int low, int high){
		
		int left = low, right = high;
		// get pivote values
		int pivot = numbers[low + (low+high)/2];

		// divide into two lists
		while (left <= right){
			//locate the left/right value to pivot
			while (numbers[left] < pivot)
				left++;
			while (numbers[right] > pivot)
				right--;

			// exchange the values
			if (left <= right) {
				swap(left,right);
				left++;
				right--;
			}
		}
			
		// recursion until right passes low & left passes high
		if (low < right)
			quicksort(low, right);
		if (high > left)
			quicksort(left, high);

	}

	public void swap (int left, int right){
		int temp = numbers[left];
		numbers[left]= numbers[right];
		numbers[rigth] = temp;
	}
}