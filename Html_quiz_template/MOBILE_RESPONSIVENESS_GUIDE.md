# Mobile Responsiveness Guide for Quiz Templates

When building or modifying HTML Quiz Templates, strictly adhere to these mobile responsiveness guidelines to ensure a flawless experience on small screens:

## 1. Viewport Meta Tag
Always include strict viewport configurations to prevent unwanted scaling and horizontal scrolling:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
```

## 2. Preventing Header Button Truncation
In the main navigation header (containing the Logo/Title and action buttons like Fold, Focus, Map):
- Ensure the container holding the Logo and Title has `min-w-0` (min-width: 0) applied. This allows the inner flex items to truncate properly using the `truncate` utility without pushing other items off-screen.
- Ensure the container holding the action buttons on the right has `flex-shrink-0`. This forces the right-hand controls to maintain their shape and size, ensuring they never get pushed out of the viewport on small screens.

**Example Fix:**
```html
<!-- Left side (Logo/Title) -->
<div class="flex items-center gap-2 md:gap-3 logo-container transition-opacity duration-300 min-w-0">
    ... <h1 class="truncate">...</h1> ...
</div>

<!-- Right side (Buttons) -->
<div class="flex items-center gap-1 md:gap-4 flex-shrink-0">
    ... buttons ...
</div>
```

## 3. Handling Fixed Footer / Bottom Navigation
If your quiz uses a fixed tab bar or bottom footer (common for "Previous" / "Next" / "Submit" buttons):
- Content containers, especially side-panels (like the Question Map panel), must account for this fixed footer.
- Apply a `padding-bottom` (e.g., `padding-bottom: 90px;`) specifically to the scrollable element (`overflow-y-auto`) inside your side panels.
- Applying padding directly to the parent wrapper might not affect the scroll bounds of inner children correctly. Always target the actual scrolling element.

**Example Fix:**
```css
/* Space for fixed bottom nav in question map to prevent hiding */
@media (max-width: 640px) {
    #question-map-panel .overflow-y-auto {
        padding-bottom: 90px;
    }
}
```

Keep these points in mind for all future UI modifications to avoid hidden elements and broken layouts on mobile devices.
