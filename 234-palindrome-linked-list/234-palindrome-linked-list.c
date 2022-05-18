/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct double_list {
    int val;
    struct double_list *next;
    struct double_list *prev;
};



bool isPalindrome(struct ListNode* head){
    struct ListNode* head_head = head; 
    struct double_list* doubly = malloc(sizeof(struct double_list));
    struct double_list* doubly_head = doubly; 
    
    while(head != NULL) {
        doubly->val = head->val; 
        struct double_list* temp = malloc(sizeof(struct double_list)); 
        doubly->next = temp; 
        temp->prev = doubly; 
        doubly = doubly->next; 
        
        head=head->next; 
    }
    head = head_head; 
    doubly = doubly->prev; 
    
    bool palindrome = true; 
    while(head != NULL) {
        if(head->val != doubly->val) {
            palindrome = false; 
        }
        head = head->next; 
        doubly = doubly->prev; 
    }
    
    return palindrome;
}