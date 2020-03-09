package aulas_ufpi;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class _Invoice {

	public static void main(String[] args) throws InterruptedException {
		Scanner sc = new Scanner(System.in);
		
		String products = "apple,ball,tv,table,smartphone,computer,book,couch";
		String prices = "0.20, 5.00, 850.00, 150.00, 600.00, 550.00, 10.00, 250.00";
		String answer, op;
		double how_many, new_price;
		Thread.currentThread();
		
		Date dataHoraAtual = new Date();
		String date = new SimpleDateFormat("dd/MM/yyyy").format(dataHoraAtual);
		String hora = new SimpleDateFormat("HH:mm:ss").format(dataHoraAtual);
		
		System.out.println("Date: " + date);
		System.out.println("Time: " + hora);
		
		String[] product = products.split(",", 8); // n = how many objects i have in my store
		String[] price = prices.split(",", 8); // n prices
				
		System.out.println("Welcome to BuyMoreWithJava, what do you want to buy?: ");
		answer = sc.next();
		int i = 0;
		
		
		do{
			if(answer.equalsIgnoreCase(product[i])){
				System.out.println("I found it!: ");
				System.out.println("It will cost: R$ " + price[i] + " per unit");
				System.out.println("How many itens do you want?: ");
				how_many = sc.nextDouble();
				double Price = Double.parseDouble(price[i]);
				new_price = Price * how_many;
				
				System.out.println("Do you agree with the Terms And Conditions for online buying?: ");
				op = sc.next();
				
				if(op.equalsIgnoreCase("yes")) {
					System.out.println("Ok!: ");
					System.out.println("Now, i'll give your invoice. Please wait: \n");
					Thread.sleep(3000);
					
					Date DataHoraAtual = new Date();
					String Date = new SimpleDateFormat("dd/MM/yyyy").format(DataHoraAtual);
					String Hora = new SimpleDateFormat("HH:mm:ss").format(DataHoraAtual);
					
					System.out.println("Date: " + Date);
					System.out.println("Time: " + Hora);
					
					System.out.println("------------------------- BR Piauí - Teresina\nProduct: .................." + product[i]);
					System.out.printf("Price: ....................R$ %.2f\n", new_price);
					sc.close();
					return;
				}else {
					System.out.println("Sorry, i can't sell to you without the conditions!");
					sc.close();
					return;
				}
			}
			
		i++;
		}while(i < 8);
		System.out.println("Sorry, i couldn't reach your search. Try again.");
		sc.close();
		
	}

}
