#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *left = *head, *right = *head;
	int len = 0, i = 0, j = 0;

	while (left)
	{
		left = left->next;
		len++;
	}
	left = *head;
	for (i = 1; i <= len; i++)
	{
		for (j = i; j <= len - i; j++)
			right = right->next;
		if (left->n != right->n)
			return (0);
		left = left->next;
		right = left;
	}
	return (1);
}
