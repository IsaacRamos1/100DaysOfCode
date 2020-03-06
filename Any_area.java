package aulas_ufpi;

import java.util.Locale;
import java.util.Scanner;
	
	//Created by IsaacRamos
	//
	//(PT-BR) Apresentando seus pontos, podemos descobrir a área de qaulquer polígono
	//conhecimentos tirados da geometria analítica são necessário para entender.
	//
	//(ENG-US) I present to you a tip on how to find any area of ​​a possible polygon. 
	//It is only necessary to present the coordinates of the points.
	//Warning: This polygon must exit!

public class Any_area {
	
	public static void main(String[] args) {
	Locale.setDefault(Locale.US);
	Scanner sc = new Scanner(System.in);
	
	int n, j;
	int point = 65;
	System.out.println("How many sides?: ");
	n = sc.nextInt();
	
	double[][] num;
	num = new double[n+1][2];
	double aux1, aux2, sum1 = 0, sum2 = 0;
	
	for(int i = 0; i < n; i++) {
		System.out.printf("Type the coordinations for the point %c (x,y): \n", (char)(point));
		for(j = 0; j < 2; j++) {	
			num[i][j] = sc.nextDouble();
			if(i == 0) {
				num[n][0] = num[0][0];
				num[n][1] = num[0][1];
			}
		}
		point++;
	}
	System.out.println("  X | Y |");
	for(int i = 0; i < n; i++) {
		for(j = 0; j < 2; j++) {
			System.out.print(num[i][j] + " | ");
		}
		System.out.println("");
	}

	for(int i = 0; i < n; i++) {
		aux1 = num[i][0] * num[i+1][1];
		sum1 = sum1 + aux1;
	}
	
	for(int i = 0; i < n; i++) {
		aux2 = num[i][1] * num[i+1][0];
		sum2 = sum2 + aux2;
	}
	double area;
	area = Math.abs((sum1 - sum2)/2);
	System.out.println("Area: " + area);
	
	sc.close();
	}
}