package com.sumeyya.main;

public interface IAnimal {
	public void eat(String food);
	public String makeSound();
	public void reproduce(IAnimal animal);
	public void play();
}
