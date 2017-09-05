package com.sumeyya.main;

public class DogAnimal extends Animal implements IAnimal {

	public DogAnimal(String name) {
		super(name);
	}
	
	@Override
	public String makeSound() {
		return "Hav hav!";
	}

	public void guard() {
		
	}

	@Override
	public void reproduce(IAnimal animal) {
		System.out.println(getName() + " mating: " + animal);
	}

	@Override
	public void play() {
		System.out.println(getName() + " Playing like a monster!");
	}

}
