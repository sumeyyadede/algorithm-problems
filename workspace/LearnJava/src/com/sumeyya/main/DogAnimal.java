package com.sumeyya.main;

public class DogAnimal extends Animal {

	public DogAnimal(String name) {
		super(name);
	}
	
	@Override
	public String makeSound() {
		return "Hav hav!";
	}

	public void guard() {
		
	}

}
