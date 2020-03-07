package aulas_ufpi;

import java.util.Locale;
import java.util.Random;
import java.util.Scanner;

public class _SocietyRule {

	public static void main(String[] args) throws InterruptedException {
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		Thread.currentThread();
		Random rand = new Random();
		
		double profit, sum = 0, aux;
		int partners, letter = 65;
		
		System.out.println("How much is the profit?: ");
		profit = sc.nextDouble();
		
		System.out.println("How many partners?: ");
		partners = sc.nextInt();
		double[] invested = new double[partners];
		double[] SingleProfit = new double[partners];
		
		for(int i = 0; i < partners; i++) {
			System.out.printf("Partner %c invested: \n", (char)letter);
			invested[i] = sc.nextDouble(); //rand.nextInt(10000);
			sum += invested[i];
			letter++;
		}
		aux = profit / sum;
		letter = 65;
		
		for(int i = 3; i > 0; i--) {	
			Thread.sleep(1000);
			System.out.println(i + "...");
		}
		Thread.sleep(2000);
		
		for(int i = 0; i < partners; i++) {
			SingleProfit[i] = invested[i] * aux;
			System.out.printf("\nPartner %c = R$ %.2f\n", (char)letter, SingleProfit[i]);
			letter++;
		}
		sc.close();
	}
}
