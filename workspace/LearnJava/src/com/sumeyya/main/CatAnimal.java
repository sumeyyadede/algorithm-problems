package com.sumeyya.main;

public class CatAnimal extends Animal implements IAnimal {

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

	@Override
	public void reproduce(IAnimal animal) {
		System.out.println(getName() + " mating: " + animal);
	}

	@Override
	public void play() {
		System.out.println(getName() + " Playing like a monster!");
	}

}
