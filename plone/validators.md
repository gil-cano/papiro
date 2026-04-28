# Validadores


## Add or Edit Form

```python
  @invariant
  def validate_email_and_user(self):
      """Check for user."""
      context = getattr(self, '__context__', None)
      if context is None:
          # We are in an AddForm
          return checkForUserlogin(self.email)
      # We are in an EditForm
      if context.email == self.email:
          # nothing has changed
          return True
      # Changes in editForm. Test if new userlogin is not assigned
      return checkForUserlogin(self.email)
```
