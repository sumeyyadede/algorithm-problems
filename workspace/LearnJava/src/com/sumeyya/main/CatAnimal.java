package com.sumeyya.main;

public class CatAnimal extends Animal {

	public CatAnimal(String name) {
		super(name);
	}

	public CatAnimal() {
		super();
	}

	@Override
	public String makeSound() {
		return "Miyav";
	}

}
