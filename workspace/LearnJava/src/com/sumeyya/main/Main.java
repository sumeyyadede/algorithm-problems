package com.sumeyya.main;

public class Main {

	public static void main(String[] args) {
		IAnimal animals[] = new IAnimal[] {
				new CatAnimal("Mahmut"),
				new DogAnimal("Ömer"),
				new HumanAnimal("Sumus")
		};
		animals[0].eat("carrot");
		animals[1].eat("tomato");
		animals[2].eat("gurka");
		
		int a = 4;
		Integer A = 5;
		System.out.println("Hello World!");
		System.out.println(a);
		for(int i = 0; i < animals.length; i++) {
			System.out.println(animals[i]);			
			System.out.println(animals[i].makeSound());
			animals[i].reproduce(animals[0]);
			animals[i].play();
		}
		Integer newNumber = Integer.parseInt("343424");
		System.out.println(newNumber);
	}

}
