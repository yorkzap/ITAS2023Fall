# Cascading Style Sheets (CSS) Overview
- CSS determines how HTML elements are displayed on a web page.
- CSS rules can conflict with each other, causing unexpected results.
- The cascade, specificity, inheritance, and rule order are factors that determine which CSS rules get applied.

## The Cascade of CSS
- The cascade determines which CSS rules take precedence.
- Default browser styles can affect how elements are styled.
- Understanding the cascade helps avoid unexpected styling results.

## Specificity
- Specificity refers to the importance of a CSS rule.
- The more specific a selector, the higher its specificity.
- Specificity helps resolve conflicts between conflicting rules.
- Specificity is determined by the type of selectors used (ID, class, type), and inline styles have the highest specificity.

## Not Everything Adds to Specificity
- Some CSS symbols and combinators (e.g., *, +, ~, >) do not add to specificity.
- The universal selector * has no specificity.

## Inheritance
- Some CSS properties are inherited by child elements.
- Inherited properties include color, font-size, and font-family.
- Directly targeting an element with a rule always beats inheritance.

## Rule Order
- In cases where all other factors are equal, the last defined CSS rule takes precedence.
- Rule order serves as a tie-breaker for equally specific rules.

## Practice and Assignment
- To practice CSS, you can style web pages using external CSS files.
- Experiment with various CSS properties like color, background color, typography, etc.
- External CSS files are recommended for styling.
- Use generic font families as fallbacks for the font-family property when specifying fonts.