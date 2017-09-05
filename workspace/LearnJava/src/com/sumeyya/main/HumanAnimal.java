package com.sumeyya.main;

public class HumanAnimal extends Animal {

	public HumanAnimal() {
		super();
	}

	public HumanAnimal(String name) {
		super(name);
	}

	@Override
	public String makeSound() {
		return "bla bla";
	}
	
	public void eat(Animal animal) {
		System.out.println("bunu yiyorum: " + animal);
		
	}
	

}
