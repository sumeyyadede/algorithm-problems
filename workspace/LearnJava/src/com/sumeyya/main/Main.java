package com.sumeyya.main;

public class Main {

	public static void main(String[] args) {
		Animal animals[] = new Animal[] {
				new Animal("Mahmut"),
				new DogAnimal("Ömer")
		};
		
		animals[0].eat("carrot");
		animals[1].eat("tomato");
//		animals[1].setName("Murtaza");
//		((DogAnimal) animals[1]).guard();
		
		int a = 4;
		Integer A = 5;
		System.out.println("Hello World!");
		System.out.println(a);
		for(int i = 0; i < animals.length; i++) {
			System.out.println(animals[i]);			
			System.out.println(animals[i].makeSound());			
		}
		Integer newNumber = Integer.parseInt("343424");
		System.out.println(newNumber);
	}

}
