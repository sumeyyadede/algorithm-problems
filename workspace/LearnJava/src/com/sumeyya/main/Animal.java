package com.sumeyya.main;

public abstract class Animal {
	
	private String name;
	private Integer age;

	public Animal() {
	}

	public Animal(String name) {
		this.name = name;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	
	public void eat(String food) {
		System.out.println(name + ": I am eating " + food);
	}
	
	public String makeSound() {
		return "Generic Sound";
	}

	@Override
	public String toString() {
		return name;
	}
	
}
