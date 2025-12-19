import React, { useEffect } from "react";
import {
  ComponentProps,
  withStreamlitConnection,
  Streamlit,
} from "streamlit-component-lib";
import { Carousel, useCarousel } from "./carousel-base";

// ChevronLeft and ChevronRight SVG icons
const ChevronLeft = ({ className }: { className?: string }) => (
  <svg className={className} xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor">
    <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
  </svg>
);

const ChevronRight = ({ className }: { className?: string }) => (
  <svg className={className} xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor">
    <path strokeLinecap="round" strokeLinejoin="round" d="m9 5 7 7-7 7" />
  </svg>
);

// Carousel Indicator Component
const CarouselIndicator = ({
  size = "md",
  framed = true,
}: {
  size?: "md" | "lg";
  framed?: boolean;
}) => {
  const { selectedIndex, scrollSnaps, api } = useCarousel();

  const sizeClasses = size === "lg" ? "gap-2" : "gap-1.5";
  const dotSizeClasses = size === "lg" ? "w-2 h-2" : "w-1.5 h-1.5";

  return (
    <div
      className={`flex items-center ${sizeClasses} ${
        framed ? "rounded-full bg-white/90 backdrop-blur-sm px-3 py-2 shadow-sm" : ""
      }`}
    >
      {scrollSnaps.map((_, index) => (
        <button
          key={index}
          onClick={() => api?.scrollTo(index)}
          className={`${dotSizeClasses} rounded-full transition-all ${
            selectedIndex === index ? "bg-gray-800" : "bg-gray-300"
          }`}
          aria-label={`Go to slide ${index + 1}`}
        />
      ))}
    </div>
  );
};

interface CarouselItem {
  image: string;
  title?: string;
  description?: string;
}

const MyCarousel = ({ args }: ComponentProps) => {
  const { items = [], variant = "md" } = args as { items: CarouselItem[]; variant?: "md" | "lg" };

  // Auto-resize the Streamlit iframe height
  useEffect(() => {
    Streamlit.setFrameHeight();
  }, [items]);

  const buttonSizeClasses = variant === "lg" ? "size-11" : "size-9";
  const iconSizeClasses = variant === "lg" ? "size-6" : "size-5";
  const buttonPositionClasses = variant === "lg" ? "left-5" : "left-4";
  const buttonPositionClassesRight = variant === "lg" ? "right-5" : "right-4";

  return (
    <div className="w-full max-w-4xl mx-auto font-sans">
      <Carousel.Root className="relative aspect-[1.6] w-full">
        {/* Previous Button */}
        <Carousel.PrevTrigger
          className={`absolute top-1/2 ${buttonPositionClasses} z-10 flex ${buttonSizeClasses} -translate-y-1/2 cursor-pointer items-center justify-center rounded-full bg-white/90 p-2 text-gray-700 shadow-md outline-none backdrop-blur-sm transition-all hover:bg-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-500 disabled:cursor-not-allowed disabled:bg-gray-200 disabled:text-gray-400`}
        >
          <ChevronLeft className={iconSizeClasses} />
        </Carousel.PrevTrigger>

        {/* Next Button */}
        <Carousel.NextTrigger
          className={`absolute top-1/2 ${buttonPositionClassesRight} z-10 flex ${buttonSizeClasses} -translate-y-1/2 cursor-pointer items-center justify-center rounded-full bg-white/90 p-2 text-gray-700 shadow-md outline-none backdrop-blur-sm transition-all hover:bg-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-500 disabled:cursor-not-allowed disabled:bg-gray-200 disabled:text-gray-400`}
        >
          <ChevronRight className={iconSizeClasses} />
        </Carousel.NextTrigger>

        {/* Indicator Dots */}
        <div className="absolute bottom-4 left-1/2 z-10 -translate-x-1/2">
          <CarouselIndicator framed size={variant} />
        </div>

        {/* Carousel Content */}
        <Carousel.Content className="gap-2">
          {items.map((item: CarouselItem, index: number) => (
            <Carousel.Item key={index} className="overflow-hidden rounded-xl relative">
              <img
                alt={item.title || `Slide ${index + 1}`}
                src={item.image}
                className="w-full h-full object-cover"
              />
              {(item.title || item.description) && (
                <div className="absolute inset-x-0 bottom-0 bg-gradient-to-t from-black/70 via-black/40 to-transparent p-6 pt-16">
                  {item.title && (
                    <h3 className="text-xl font-semibold text-white mb-1">
                      {item.title}
                    </h3>
                  )}
                  {item.description && (
                    <p className="text-sm text-white/90">
                      {item.description}
                    </p>
                  )}
                </div>
              )}
            </Carousel.Item>
          ))}
        </Carousel.Content>
      </Carousel.Root>
    </div>
  );
};

export default withStreamlitConnection(MyCarousel);
