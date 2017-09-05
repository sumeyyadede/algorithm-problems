package com.sumeyya.main;

public class HumanAnimal extends Animal implements IAnimal {

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

	@Override
	public void reproduce(IAnimal animal) {
		System.out.println(getName() + " mating: " + animal);
	}

	@Override
	public void play() {
		System.out.println(getName() + " Playing like a monster!");
	}

}
