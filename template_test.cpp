template <class T> 
class StackMin:public Stack{
public:
	StackMin(){
		stack_Min = new Stack<>;
	}
	T push(T);
	T pop();
	T stack_min();

private:
	Stack<T>* stack_Min;
};

template <class T> 
int StackMin<T>::push(T data){
	Stack<Node>* n;
	n = Stack<T>::push(data);
	if(stack_Min->Stack<T>::isEmpty() || stack_Min->peek().data > n->data){
		stack_Min->push(n);
	}
}
template <class T>
T StackMin<T>::push(T data){
	Stack<T>::push(data);
	Node<T>* n;
	n = Stack<T>::getHead();
	if(stack_Min->isEmpty() || stack_Min->peek()->data > n->data){
		stack_Min->push(n);
	}
}
template <class T>
T StackMin<T>::pop(){
	if (Stack<Stack<T>>::peekNode() == stack_Min->peek()){
		stack_Min->pop();
	}
	return Stack<Stack<T>>::pop();
}
template <class T>
T StackMin<T>::stack_min(){
	if(stack_Min->isEmpty()){
		return stack_Min->peek();
	}
	return NULL_VALUE;
}
