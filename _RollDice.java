package aulas_ufpi;

import java.util.Random;

public class _RollDice {
		//base on PDF taken from https://sites.google.com/site/profnewtonjava
		
	public static void main(String[] args) {
		//Function Random
		final int epochs = 100;
		int epoch[] = new int[epochs];
		int cont1, cont2, cont3, cont4, cont5, cont6;
		cont1 = cont2 = cont3 = cont4 = cont5 = cont6 = 0;
		float total;
		Random rand = new Random();
		
		for(int i = 0; i < epochs; i++) {
			epoch[i] = rand.nextInt(6) + 1;
			switch(epoch[i]) {
			case 1:
				cont1++;
				break;
			case 2:
				cont2++;
				break;
			case 3:
				cont3++;
				break;
			case 4:
				cont4++;
				break;
			case 5:
				cont5++;
				break;
			case 6:
				cont6++;
				break;
			}	
		}
		
		System.out.println("Result: ");
		System.out.printf("Face 1: %d times = %.2f %%\n", cont1, (float) cont1/epochs * 100);
		System.out.printf("Face 2: %d times = %.2f %%\n", cont2, (float) cont2/epochs * 100);
		System.out.printf("Face 3: %d times = %.2f %%\n", cont3, (float) cont3/epochs * 100);
		System.out.printf("Face 4: %d times = %.2f %%\n", cont4, (float) cont4/epochs * 100);
		System.out.printf("Face 5: %d times = %.2f %%\n", cont5, (float) cont5/epochs * 100);
		System.out.printf("Face 6: %d times = %.2f %%\n", cont6, (float) cont6/epochs * 100);
		
		total = (float) cont1/epochs * 100 + (float) cont2/epochs * 100 + (float) cont3/epochs * 100
				+ (float) cont4/epochs * 100 + (float) cont5/epochs * 100 + (float) cont6/epochs * 100;
		
		System.out.printf("Total %d = %.2f %%", epochs, total);
	}
}
